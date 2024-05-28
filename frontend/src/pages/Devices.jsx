import { useState } from 'react';
import DataTableComponent from '../components/Datatable/Table';

export default function Devices() {
  const [details, setDetails] = useState({
    method: 'POST',
    title: 'Add Device',
    btnName: 'Add Device',
    uri: '/devices',
    loadField: { name: {id: 'Name'}, active: { id: 'Active', ids: [{ id: 'Yes', name: 'Y' }, { id: 'No', name: 'N' }] }}
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
      name: 'Active',
      selector: row => row.active === 'Y' ? 'Yes' : 'No',
      sortable: true,
    },
    {
      name: 'Actions',
      cell: (row) => (
        <div>
          <button className="btn btn-success me-2" onClick={() => onTriggerEdit(row.id, { name: row.name, active: row.active })}>
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
      uri: `/devices/${row_id}`,
      method: 'DELETE',
      btnName: 'Add Device',
    });
    setModelProperties({
      title: 'Confirm Delete',
      message: 'Are you sure you want to delete this device?',
      isTimeout: false
    });
    setModelOpts({ onClickHandler: 1 });
    setShowConfModal(true);
  };

  const onTriggerEdit = (row_id, row) => {
    setDetails({
      method: 'PUT',
      uri: `/devices/${row_id}`,
      btnName: 'Add Device',
      title: 'Update Device',
      loadField: {
        name: { id: 'Name', name: row.name },
        active: { ids: [{ id: 'Yes', name: 'Y' }, { id: 'No', name: 'N' }], name: row.active }
      }
    });
    setShowFormModal(true);
  };

 

  return (
    <div className="App">
      <h1 className="fs-5 text-light fw-light mb-3">Devices</h1>
      <DataTableComponent 
        uri={"/devices"}
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
