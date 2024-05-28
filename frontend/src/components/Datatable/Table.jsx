import React, { useEffect, useState } from 'react';
import { useQuery, useMutation } from '@tanstack/react-query';
import { process_request } from "../../utils/request.axios";
import DataTable from 'react-data-table-component';
import Spinner from '../Spinner';
import FormModal from '../Modal/Form';
import Confirmation from '../Modal/Confirmation';
import { Button } from 'react-bootstrap';


const DataTableComponent = ({ uri, columns, details, fnUpdateDetails, showFormModalProp, showConfModalProp, modelProperties, modelOpts }) => {
  const [defaultDetails, setDefaultDetails] = useState(details)
  const [showFormModal, setShowFormModal] = useState(showFormModalProp);
  const [showConfModal, setShowConfModal] = useState(showConfModalProp);
  const [modalProps, setModalProps] = useState(modelProperties);
  const [modalOpts, setModalOpts] = useState(modelOpts);

  useEffect(() => {
    if (details.method === 'PUT') {
      setShowFormModal(true);
    } else if (details.method === 'DELETE') {
      setModalProps(modelProperties)
      setModalOpts(modelOpts)
      setShowConfModal(true);
    }
    
    
  }, [details, modelProperties, modelOpts]);
  
  const fetchData = async () => {
    let response = await process_request({ uri, method: 'GET', data: [] })
    return response.data
  }
  const { isLoading, isError, data, refetch } = useQuery({
    queryKey: [uri],
    queryFn: fetchData,
    refetchInterval: 1000,
  });

  let modalObj = { 'props': setModalProps, 'opts': setModalOpts }
  let mutation = useMutation({ 
    mutationFn: () => process_request({ uri: details.uri, data: [], method: details.method, return_obj: {show: setShowConfModal, response: modalObj} }),
    onSuccess: () => () => refetch 
  });


  const resetModalConfig = () => {
    setModalOpts(false)
  }

  const resetDefaultDetails = () => {
    fnUpdateDetails(defaultDetails)
    setShowFormModal(true)
  }

  const handleConfirmDelete = () => {
      mutation.mutateAsync();
      setShowConfModal(false);
      
  };

  if (isLoading) {
    return <Spinner />;
  }

  if (isError) {
    return <p>Restart server....</p>;
  }

  return (
    <>
      {details && (
        <Button variant="primary" className="mb-2" onClick={() => resetDefaultDetails()}>
          {details.btnName}
        </Button>
      )}

      <FormModal
        show={showFormModal}
        handleClose={() => setShowFormModal(false)}
        details={details}
        fnShowConfModal={setShowConfModal}
        fnResetModalConfig={resetModalConfig}
        fnConfModalData={modalObj}
        fnRefetch={refetch}
      />
    
      <Confirmation
        show={showConfModal}
        handleClose={() => setShowConfModal(false)}
        modelProperties={modalProps}
        handleDelete={handleConfirmDelete}
        modelOpts={modalOpts}
      />

      <div className="table small rounded-2 data-table-container">
        <DataTable
          columns={columns}
          data={data}
          pagination
          highlightOnHover
        />
      </div>
    </>
  );
};

export default DataTableComponent;
