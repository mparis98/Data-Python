<script>
import {
    Bar
} from 'vue-chartjs';
import {
    reactiveProp
} from '../mixins';

export default {
    name: 'MyBar',
    extends: Bar,
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
