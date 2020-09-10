<template>
<div id="app">
    <img id="logo" src="../assets/logo.png">
    <ul id="menu">
        <li data-menuanchor="page1" class="active"><a href="#page1">Section 1</a></li>
        <li data-menuanchor="page2"><a href="#page2">Statistique</a></li>
        <li data-menuanchor="page3"><a href="#page3">Entreprise 2020</a></li>
        <li>
            <a href="https://github.com/mparis98/Data-Python" target="_blank" rel="noopener" class="twitter-share">
                <img height="25px" src="../assets/github.png">
            </a>
        </li>
    </ul>

    <full-page :options="options" id="fullpage">
        <div class="section">
        </div>
        <div class="section">
            <div class="slide">
                <h3>Activité dominant après la crise de Covid-19</h3>
                <div id="parent">
                    <grid :auto-width="autoWidth" :cols="colsCodeApe" :pagination="paginationCodeApe" :rows="codeAPE" :search="search"></grid>
                    <MyBar :chart-data="dataPoints" />
                </div>
            </div>
            <div class="slide">
                <h3>Création d'entreprises par région</h3>
                <div id="parent">
                    <MyLine :chart-data="dataPointsRegion" />
                </div>
            </div>
            <div class="slide">
                <h3>Slide 2.3</h3>
            </div>
        </div>
        <div class="section">
            <h1>Entreprises 2020</h1>
            <grid :auto-width="autoWidth" :cols="cols" :pagination="pagination" :rows="companys" :search="search" :sort="sort"></grid>
        </div>
    </full-page>
</div>
</template>

<script>
import axios from 'axios';
import Grid from '../../node_modules/gridjs-vue/src/gridjs-vue';
import MyBar from "./MyBar";
import MyLine from "./MyLine";

export default {
    name: 'app',
    components: {
        Grid,
        MyBar,
        MyLine,
    },
    data() {
        return {
            companys: [],
            countsApe: [],
            countsHits: [],
            codeAPE: [],
            autoWidth: true,
            dataPoints: {},
            dataPointsRegion: {},
            search: true,
            sort: true,
            url: 'http://localhost:5000/company/',
            urlCount: 'http://localhost:5000/company/count/',
            urlCodeApe: 'http://localhost:5000/codeape/',
            urlCountRegion: 'http://localhost:5000/company/count/region/',
            cols: ['Siren', 'Denomination', 'Region', 'Ville', 'Code_Postal', 'Date_Immatriculation', 'Code_Ape'],
            pagination: {
                limit: 8
            },
            colsCodeApe: ['Code_Ape', 'Intitule_Naf'],
            paginationCodeApe: {
                limit: 1
            },
            options: {
                licenseKey: 'YOUR_KEY_HERE',
                afterLoad: this.afterLoad,
                scrollOverflow: true,
                scrollBar: false,
                menu: '#menu',
                navigation: true,
                anchors: ['page1', 'page2', 'page3'],
                sectionsColor: ['#41b883', '#1bcee6', '#e5e7eb', '#fec401', '#1bcee6', '#ee1a59', '#2c3e4f', '#ba5be9', '#b4b8ab']
            },
        }
    },
    methods: {
        afterLoad() {
            console.log('After load')
        },
        addSection(e) {
            e.preventDefault()
            var newSectionNumber = document.querySelectorAll('.fp-section').length + 1
            // creating the section div
            var section = document.createElement('div')
            section.className = 'section'
            section.innerHTML = `<h3>Section ${newSectionNumber}</h3>`
            // adding section
            document.querySelector('#fullpage').appendChild(section)
            // creating the section menu element
            var sectionMenuItem = document.createElement('li')
            sectionMenuItem.setAttribute('data-menuanchor', 'page' + newSectionNumber)
            sectionMenuItem.innerHTML = `<a href="#page${newSectionNumber}">Section${newSectionNumber}</a>`
            // adding it to the sections menu
            var sectionsMenuItems = document.querySelector('#menu')
            sectionsMenuItems.appendChild(sectionMenuItem)
            // adding anchor for the section
            this.options.anchors.push(`page${newSectionNumber}`)
            // we have to call `update` manually as DOM changes won't fire updates
            // requires the use of the attribute ref="fullpage" on the
            // component element, in this case, <full-page>
            // ideally, use an ID element for that element too
            this.$refs.fullpage.build()
        },
        removeSection() {
            var sections = document.querySelector('#fullpage').querySelectorAll('.fp-section')
            var lastSection = sections[sections.length - 1]
            // removing the last section
            lastSection.parentNode.removeChild(lastSection)
            // removing the last anchor
            this.options.anchors.pop()
            // removing the last item on the sections menu
            var sectionsMenuItems = document.querySelectorAll('#menu li')
            var lastItem = sectionsMenuItems[sectionsMenuItems.length - 1]
            lastItem.parentNode.removeChild(lastItem)
        },
        toggleNavigation() {
            this.options.navigation = !this.options.navigation
        },
        toggleScrollbar() {
            console.log('Changing scrollbar...')
            this.options.scrollBar = !this.options.scrollBar
        },
        getCompanys() {
            axios.get(this.url)
                .then((result) => {
                    this.companys = result.data.data
                })
        },
        getCountsApe() {
            axios.get(this.urlCount)
                .then((result) => {
                    this.countsApe = result.data[0]
                })
        },
        getCountsHits() {
            axios.get(this.urlCount)
                .then((result) => {
                    this.countsHits = result.data[1]
                })
        },
        getCodeApe() {
            axios.get(this.urlCodeApe)
                .then((result) => {
                    this.codeAPE = result.data.data

                })
        },
        getCountsRegion() {
            axios.get(this.urlCountRegion)
                .then((result) => {
                    this.countsRegion = result.data[0]
                })
        },
        getCountsRegionHits() {
            axios.get(this.urlCountRegion)
                .then((result) => {
                    this.countsRegionHits = result.data[1]
                })
        },
        fillData() {
            this.dataPoints = {
                labels: this.countsApe,
                datasets: [{
                    label: 'Codes APE',
                    backgroundColor: '#f87979',
                    data: this.countsHits
                }]
            }
        },
        fillDataRegion() {
            this.dataPointsRegion = {
                labels: this.countsRegion,
                datasets: [{
                    label: 'Regions',
                    backgroundColor: "blue",
                    data: this.countsRegionHits
                }]
            }
        },
    },
    mounted() {
        this.getCompanys(),
            this.getCountsApe(),
            this.getCodeApe(),
            this.getCountsHits(),
            this.getCountsRegion(),
            this.getCountsRegionHits(),
            setInterval(() => {
                this.fillData()
            }, 2000),
            setInterval(() => {
                this.fillDataRegion()
            }, 2000)
    }
}
</script>

<style>
#parent {
    max-width: 1300px;
    margin: auto;
}

#bar-chart,
#line-chart {
    max-width: 1300px;
}

#menu {
    position: fixed;
    width: 100%;
    top: 0px;
    z-index: 70;
    -webkit-font-smoothing: antialiased;
    -moz-font-smoothing: antialiased;
    letter-spacing: 1px;
    font-size: 1.1em;
    padding-top: 15px;
    padding-bottom: 15px;
    margin-top: 0px;
    background-color: #00000085;
}

#menu li a {
    color: #fff;
}

#logo {
    position: fixed;
    top: 6px;
    left: 20px;
    height: 50px;
    z-index: 99;
    -webkit-font-smoothing: antialiased;
    -moz-font-smoothing: antialiased;
}

@media (max-width: 979px) {
    #logo {
        display: none;
    }
}

h1 {
    color: #fff;
}

h3 {
    color: #fff;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    display: inline-block;
    margin: 0 10px;
}

a {
    color: black;
    text-decoration: none;
}

ul .active {
    text-decoration: underline;
}
</style>
