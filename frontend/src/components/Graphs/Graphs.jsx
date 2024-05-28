import Bar from "./Bar";
import PieChart from "./PieChart";
import { useQuery } from "@tanstack/react-query";
import { process_request } from "../../utils/request.axios";
import Spinner from "../Spinner";


export default function Graphs(){
    const graphDefs = [
        { uri: '/parameters/device/parameter/split', method: 'GET', data: [] },
        { uri: '/parameters/top/10/parameters', method: 'GET', data: [] },
    ];
    
    const fetchGraphData = async () => {
    const stats = await Promise.all(graphDefs.map(async (stat) => {
        const result = await process_request({ uri: stat.uri, method: stat.method, data: stat.data });
            return result.data;
        }));
    
        return stats;
    };
    
    const { isLoading, isError, data } = useQuery({
        queryKey: ["DashboardCards"],
        queryFn: fetchGraphData,
    });

    return(
        <>
           { isLoading && <Spinner /> }
            { isError && <p>Restart server....</p> }
            { data && <div className="row p-1 py-2">
                <div className="col-md-6">
                <div className="card border-0card rounded-2 p-3">
                    <h6 className="fs-5 fw-bold text-dp">Top 10 Device Parameters</h6>
                    {<Bar data={data[0]}/> }
                </div>
                </div>  
                <div className="col-md-6">
                <div className="card card rounded-2 p-3">
                    <h6 className="fs-5 fw-bold text-dp">Parameter Split Per Device</h6>
                    { <PieChart data={data[1]}/> }
                </div>  
                </div>  
            </div>  }
        </>
    )
    
}
