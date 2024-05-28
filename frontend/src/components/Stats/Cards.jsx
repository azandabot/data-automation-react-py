import { useQuery } from "@tanstack/react-query";
import { process_request } from "../../utils/request.axios";
import Stats from "./Stats";
import Spinner from "../Spinner";

export default function Cards(){
    const statDefinitions = [
        { id: 1, title: 'Total Parameters', bg: 'bg-warning', uri: '/parameters/total', method: 'GET', data: [], icon: 'braces-asterisk' },
        { id: 2, title: 'Total Devices', bg: 'bg-primary', uri: '/devices/total', method: 'GET', data: [], icon: 'hdd-rack' },
        { id: 3, title: 'Most Frequent Parameter', bg: 'bg-success', uri: '/parameters/frequent/most', method: 'GET', data: [], icon: 'arrow-up-circle' },
        { id: 4, title: 'Least Frequent Parameter', bg: 'bg-danger', uri: '/parameters/frequent/least', method: 'GET', data: [], icon: 'arrow-down-circle' },
    ];

    const fetchStats = async () => {
    const stats = await Promise.all(statDefinitions.map(async (stat) => {
        const result = await process_request({ uri: stat.uri, method: stat.method, data: stat.data });
            return {
                id: stat.id,
                bg: stat.bg,
                title: stat.title,
                total: result.data,
                icon: stat.icon
            };
        }));

        return stats;
    };

    
    const { isLoading, isError, data } = useQuery({
        queryKey: ["DashboardStats"],
        queryFn: fetchStats,
    });
    return (
    <>
        {isLoading && <Spinner />}
        {isError && <p>Error loading data. Please restart the server.</p>}
        <div className="row">
          {data && data.length > 0 && data.map((stat) => (
              <div className={`col-md-3`}  key={stat.id}>
                  <Stats key={stat.id} data={stat} />
              </div>
          ))}
        </div>
    </>
    )
    
}