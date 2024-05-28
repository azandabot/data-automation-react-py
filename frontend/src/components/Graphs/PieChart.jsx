import { Pie } from '@ant-design/plots';

export default function PieChart({ data }) {
  
  const config = {
    data,
    angleField: 'total',
    colorField: 'name',
    legend: {
      color: {
        title: false,
        position: 'right',
        rowPadding: 5,
      },
    },
    height: 300
  };
  return <Pie {...config} />;
};