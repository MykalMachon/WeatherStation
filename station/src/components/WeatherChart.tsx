import { Chart as ChartJS, Tooltip, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js';
import { Line } from 'react-chartjs-2';

type WeatherChartProps = {
  data: Array<any>;
};

ChartJS.register({
  Tooltip,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
})

const WeatherChart = ({ data }: WeatherChartProps) => {
  const options = {
    responsive: true,
  };

  const labels = data.map((data) => data['created_at']);

  const chartData = {
    labels,
    datasets: [
      {
        label: 'Temperature (Pressure)',
        data: data.map((data) => data.temperature_pres),
        borderColor: 'rgb(119, 101, 240)',
        tension: 0.1,
      },
      {
        label: 'Temperature (Humidity)',
        data: data.map((data) => data.temperature_hum),
        borderColor: 'rgb(240, 101, 157)',
        tension: 0.1,
      },
    ],
  };

  return (
    <section>
      <Line data={chartData} options={options} />
    </section>
  );
};

export default WeatherChart;
