import { useState, useEffect } from 'react';
import { Modal, Button } from 'react-bootstrap';

const Confirmation = ({ show, handleClose, handleDelete, modelProperties, modelOpts }) => {
    const [state, setState] = useState(show);

    useEffect(() => {
        let timer;
        if (modelProperties?.isTimeout) {
            timer = setTimeout(() => {
                setState(false);  
                handleClose();  
            }, 1500);
        }
        return () => clearTimeout(timer);
    }, [modelProperties?.isTimeout]);

    useEffect(() => {
        setState(show);
    }, [show]);

    return (
        <Modal show={state} onHide={handleClose}>
            <Modal.Header closeButton>
                <Modal.Title>{modelProperties?.title}</Modal.Title>
            </Modal.Header>
            <Modal.Body>{modelProperties?.message}</Modal.Body>
            { modelProperties?.title?.includes("Delete") && modelOpts?.onClickHandler && 
                <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Cancel
                    </Button>
                    <Button variant="danger" onClick={handleDelete}>
                        Confirm
                    </Button>
                </Modal.Footer>
            }
        </Modal>
    );
};

export default Confirmation;
