import Card from 'react-bootstrap/Card';

export default function Stats({ data }) {
  let cardClassText = typeof(data?.total) !== 'string' ? 'py-2' : ''
  let cardClassIcon = typeof(data?.total) !== 'string' ? 'display-3' : 'display-5'
  return (
        
          <Card
           
            className={`mb-2 text-white shadow bg-dp-header border-0 rounded-3`}
          >
            <Card.Body>
              <Card.Title> {data.title}</Card.Title>
              <div className="row">
              {typeof(data.total) === 'string' && <small className='text-end text-capitalize '>{data.total.split(':')[0]}</small>}

                <div className="col-md-4">
                  <i className={`bi bi-${data.icon} text-lime ${cardClassIcon} text-start`} />
                </div>

                <div className="col-md-8">
                  <Card.Text className={`text-end fs-1 fw-bolder ${cardClassText}`}>{typeof(data.total) === 'string' ? data.total.split(':')[1] : data.total}</Card.Text>
                </div>


              </div>
            </Card.Body>
          </Card>
    );
}
