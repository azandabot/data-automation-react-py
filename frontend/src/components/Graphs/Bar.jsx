import { Column } from '@ant-design/plots';

export default function Bar({ data }) {
  const config = {
    data,
    xField: 'name',
    yField: 'total',
    style: {
      fill: ({ name }) => {
        return 'rgb(72, 248, 183)';
      },
    },
    legend: false,
    height: 300
  };
  return <Column {...config} />;
};

