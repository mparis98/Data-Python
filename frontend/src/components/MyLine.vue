<script>
import {
    Line
} from 'vue-chartjs';
import {
    reactiveProp
} from '../mixins';

export default {
    name: 'MyLine',
    extends: Line,
    mixins: [reactiveProp],
    data: () => ({
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    }),

    mounted() {
        this.renderChart(this.chartData, this.options)
    }
}
</script>
