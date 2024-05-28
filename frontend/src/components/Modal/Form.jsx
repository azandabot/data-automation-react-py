import React, { useState, useEffect } from 'react';
import { Modal, Button, Form, Spinner } from 'react-bootstrap';
import { useMutation } from '@tanstack/react-query';
import { process_request } from '../../utils/request.axios';

const FormModal = ({ show, handleClose, fnResetModalConfig, fnShowConfModal, fnConfModalData, details, fnRefetch }) => {
  const [formData, setFormData] = useState({});
  const [loading, setLoading] = useState(true);
  const [options, setOptions] = useState({});

  useEffect(() => {
    const fetchOptions = async () => {
      setLoading(true);
      const newOptions = {};
      for (const field in details.loadField) {
        const value = details?.loadField[field].uri;
        if (typeof value === 'string' && value.startsWith('/')) {
          try {
            const response = await process_request({ uri: value, data: [], method: 'GET' });
            newOptions[field] = Array.isArray(response.data) ? response.data : [];
          } catch (error) {
            console.error(`Error fetching ${field}:`, error);
            newOptions[field] = [];
          }
        }
      }
      setOptions(newOptions);
      setLoading(false);
    };

    if (show) {
      fetchOptions();
    }
  }, [details.loadField, show]);

  const mutation = useMutation({
    mutationFn: (formData) => process_request({
      uri: details.uri,
      data: formData,
      method: details.method,
      return_obj: { show: fnShowConfModal, response: fnConfModalData }
    })
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await mutation.mutateAsync(formData);
    setFormData({})
    handleClose();
    fnRefetch();
    fnResetModalConfig();
  };

  return (
    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>{details.title}</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        {loading ? <Spinner animation="border" /> : (
          <Form method="POST" onSubmit={handleSubmit}>
            {details?.loadField && Object.entries(details.loadField).map(([field, value]) => (
              <Form.Group key={field} className='mb-2'>
                <Form.Label className='text-capitalize'>{value.id}</Form.Label>
                {options[field] || value?.ids ? (
                  <Form.Control
                    as="select"
                    name={field}
                    value={formData[field] || value.name || ''}
                    onChange={handleChange}
                  >
                    <option value="">Choose...</option>
                    { options[field] ? options[field].map(option => (
                      <option key={option.id} value={option.id}>
                        {option.name}
                      </option>
                    )) : value?.ids?.map(option => (
                      <option key={option.id} value={option.name[0]}>
                        {option.name}
                      </option>
                    ))}
                  </Form.Control>
                ) : (
                  <Form.Control
                    type="text"
                    name={field}
                    value={formData[field] || value.name || ''}
                    onChange={handleChange}
                  />
                )}
              </Form.Group>
            ))}
            <Button variant="primary" className='w-100 mt-3' type="submit">
              Save
            </Button>
          </Form>
        )}
      </Modal.Body>
    </Modal>
  );
};

export default FormModal;
