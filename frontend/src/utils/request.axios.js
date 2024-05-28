import axios from 'axios';

export const process_request = async ({ uri, method, data, return_obj }) => {
  try {
    const baseURL = import.meta.env.VITE_API_URL;  // Updated to use Vite environment variable
    const url = `${baseURL}${uri}`;
    
    const headers = {
      'Content-Type': 'application/json',
      // Add other headers here if needed
    };

    let response;
    switch (method) {
      case 'GET':
        response = await axios.get(url, { headers });
        break;
      case 'POST':
        response = await axios.post(url + '/', data, { headers });
        break;
      case 'PUT':
        response = await axios.put(url + '/', data, { headers });
        break;
      case 'DELETE':
        response = await axios.delete(url + '/', { headers });
        break;
      default:
        throw new Error('Invalid method');
    }
    
    return_obj?.show(true)
    return_obj?.response.props({ isTimeout: true, title: "Success", message: response.data.message })
  
    return response.data;
  } catch (error) {
     return_obj?.response.props({ isTimeout: true, title: "Error", message: "Could not process request." })
  }
};
