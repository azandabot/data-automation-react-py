import { useState } from 'react';
import DataTableComponent from '../components/Datatable/Table';

export default function Parameters() {
  const [details, setDetails] = useState({
    method: 'POST',
    btnName: 'Add Parameter',
    title: 'Add Parameter',
    uri: '/parameters',
    loadField: {
      name: { id: 'Name' },
      device_id: { id: 'Device', value: '', uri: '/devices' }, // Assuming device_id needs to fetch from an endpoint
      value: { id: 'Value' },
    }
  });

  const [showFormModal, setShowFormModal] = useState(false);
  const [showConfModal, setShowConfModal] = useState(false);
  const [modelProperties, setModelProperties] = useState({});
  const [modelOpts, setModelOpts] = useState([]);

  const columns = [
    {
      name: 'ID',
      selector: row => row.id,
      sortable: true,
    },
    {
      name: 'Name',
      selector: row => row.name,
      sortable: true,
    },
    {
      name: 'Value',
      selector: row => row.value,
      sortable: true,
    },
    {
      name: 'Type',
      selector: row => row.type,
      sortable: true,
    },
    {
      name: 'Actions',
      cell: (row) => (
        <div>
          <button className="btn btn-success me-2" onClick={() => onTriggerEdit(row.id, { name: row.name, value: row.value, device_id: row.device_id })}>
            <i className='bi bi-pen-fill text-light' />
          </button>

          <button className="btn btn-danger me-2" onClick={() => onTriggerDelete(row.id)}>
            <i className='bi bi-trash-fill text-light' />
          </button>
        </div>
      ),
    },
  ];

  const onTriggerDelete = (row_id) => {
    setDetails({
      uri: `/parameters/${row_id}`,
      method: 'DELETE',
      btnName: 'Delete Parameter',
      loadField: {} // No need to load fields for delete
    });
    setModelProperties({
      title: 'Confirm Delete',
      message: 'Are you sure you want to delete this parameter?',
      isTimeout: false
    });
    setModelOpts({ onClickHandler: 1 });
    setShowConfModal(true);
  };

  const onTriggerEdit = (row_id, row) => {
    console.log(row)
    setDetails({
      method: 'PUT',
      uri: `/parameters/${row_id}`,
      title: 'Update Parameter',
      btnName: 'Add Parameter',
      loadField: {
        name: { id: 'Name', name: row.name },
        device_id: { id: 'Device', name: row.device_id, uri: '/devices' },
        value: { id: 'Value', name: row.value },
      }
    });
    setShowFormModal(true);
  };

  return (
    <div className="App">
      <h1 className="fs-5 text-light fw-light mb-3">Parameters</h1>
      <DataTableComponent 
        uri={"/parameters"}
        columns={columns}
        details={details}
        fnUpdateDetails={setDetails}
        showFormModalProp={showFormModal}
        showConfModalProp={showConfModal}
        modelProperties={modelProperties}
        modelOpts={modelOpts}
      />
    </div>
  );
}
