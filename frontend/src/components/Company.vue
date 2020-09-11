<template>
<div id="app">
    <img id="logo" src="../assets/logo.png">
    <ul id="menu">
        <li data-menuanchor="page1" class="active"><a href="#page1">Section 1</a></li>
        <li data-menuanchor="page2"><a href="#page2">Statistique</a></li>
        <li data-menuanchor="page3"><a href="#page3">Entreprises</a></li>
        <li>
            <a href="https://github.com/mparis98/Data-Python" target="_blank" rel="noopener" class="twitter-share">
                <img height="25px" src="../assets/github.png">
            </a>
        </li>
    </ul>

    <full-page :options="options" id="fullpage">
        <div class="section">
            <div class="button">
                <a class="danger" @click="remove()">Vider les données</a>
                <a class="info" @click="generateCodeApe()">Générer les Code APE</a>
            </div>
            <div class="pure-form">
                <fieldset>
                    <input type="number" placeholder="2019" @keyup.enter="generateCompany" v-model="year" title="Année de création">
                    <input type="number" placeholder="10" @keyup.enter="generateCompany" v-model="rows" title="Nombre de lignes">
                    <input type="number" placeholder="6" @keyup.enter="generateCompany" v-model="mouth" title="Mois ciblé">
                    <button type="submit" class="pure-button pure-button-primary" @click="generateCompany">Générer les données</button>
                </fieldset>
            </div>
            <div>
                <Progress :transitionDuration="5000" :radius="80" :strokeWidth="20" value="100">
                    <div class="content">{{ nhits == '' ? 'Undefined' : nhits }}</div>
                    <template v-slot:footer>
                        <b>Nombre d'entreprise créées en {{ year }}</b>
                    </template>
                </Progress>
            </div>
            <div id="main">
                <div id="wide">
                    <Progress :transitionDuration="4000" :radius="60" :strokeWidth="15" value="10">
                        <div class="content">{{ nhits2019 == '' ? 'Undefined' : nhits2019 }}</div>
                        <template v-slot:footer>
                            <b>Nombre d'entreprise créées le {{year}}-0{{mouth}}</b>
                        </template>
                    </Progress>
                </div>
                <div id="narrow">
                    <Progress :transitionDuration="4000" :radius="60" :strokeWidth="15" value="15">
                        <div class="content">{{ nhits2020 == '' ? 'Undefined' : nhits2020 }}</div>
                        <template v-slot:footer>
                            <b>Nombre d'entreprise créées le {{year-1}}-0{{mouth}}</b>
                        </template>
                    </Progress>
                </div>
            </div>
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
                <h3>Création d'entreprises en Ile-de-France</h3>
                <div id="parent">
                    <MyLine :chart-data="dataPointsIleDeFrance" />
                </div>
            </div>
        </div>
        <div class="section">
            <h1>Entreprises</h1>
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
import Progress from "./Circulare";

export default {
    name: 'app',
    components: {
        Grid,
        MyBar,
        MyLine,
        Progress
    },
    data() {
        return {
            companys: [],
            countsApe: [],
            countsIleDeFrance: [],
            countsIleDeFranceHits: [],
            countsHits: [],
            codeAPE: [],
            nhits: '',
            nhits2019: '',
            nhits2020: '',
            year: '',
            rows: '',
            mouth: '',
            autoWidth: true,
            dataPoints: {},
            dataPointsRegion: {},
            dataPointsIleDeFrance: {},
            search: true,
            sort: true,
            url: 'http://localhost:5000/company/',
            urlCount: 'http://localhost:5000/company/count/',
            urlCodeApe: 'http://localhost:5000/codeape/',
            urlCountRegion: 'http://localhost:5000/company/count/region/',
            urlCountIleDeFrance: 'http://localhost:5000/company/count/IleDeFrance/',
            urltruncate: 'http://localhost:5000/company/truncate/',
            urlGenerateCodeape: 'http://localhost:5000/codeape/init',
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
                sectionsColor: ['#1bcee6', '#41b883', '#e5e7eb', '#fec401', '#1bcee6', '#ee1a59', '#2c3e4f', '#ba5be9', '#b4b8ab']
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
        getCountsIleDeFrance() {
            axios.get(this.urlCountIleDeFrance)
                .then((result) => {
                    this.countsIleDeFrance = result.data[0]
                })
        },
        getCountsIleDeFranceHits() {
            axios.get(this.urlCountIleDeFrance)
                .then((result) => {
                    this.countsIleDeFranceHits = result.data[1]
                })
        },
        generateCompany() {
            axios.all([
                    axios.get("https://opendata.datainfogreffe.fr/api/records/1.0/search/?dataset=societes-immatriculees-" + this.year + "&q=&rows=1&sort=date_immatriculation&facet=siren&facet=forme_juridique&facet=code_ape&facet=ville&facet=region&facet=greffe&facet=date_immatriculation&facet=statut"),
                    axios.get("https://opendata.datainfogreffe.fr/api/records/1.0/search/?dataset=societes-immatriculees-" + this.year + "&q=&rows=1&sort=date_immatriculation&facet=siren&facet=forme_juridique&facet=code_ape&facet=ville&facet=region&facet=greffe&facet=date_immatriculation&facet=statut&refine.date_immatriculation=" + this.year + "-0" + this.mouth),
                    axios.get("https://opendata.datainfogreffe.fr/api/records/1.0/search/?dataset=societes-immatriculees-" + (this.year - 1) + "&q=&rows=1&sort=date_immatriculation&facet=siren&facet=forme_juridique&facet=code_ape&facet=ville&facet=region&facet=greffe&facet=date_immatriculation&facet=statut&refine.date_immatriculation=" + (this.year - 1) + "-0" + this.mouth),
                    axios.post("http://localhost:5000/company/init/" + this.year + "_" + this.rows + "_" + this.mouth)
                ])
                .then(axios.spread((res1, res2, res3, res4) => {
                    this.nhits = res1.data.nhits;
                    this.nhits2019 = res2.data.nhits;
                    this.nhits2020 = res3.data.nhits;
                    this.getCompanys();
                    this.getCountsApe();
                    this.getCodeApe();
                    this.getCountsHits();
                    this.getCountsRegion();
                    this.getCountsRegionHits();
                    this.getCountsIleDeFrance();
                    this.getCountsIleDeFranceHits();
                    setInterval(() => {
                        this.fillData()
                    }, 1000);
                    setInterval(() => {
                        this.fillDataRegion()
                    }, 1000);
                    setInterval(() => {
                        this.fillDataIleDeFrance()
                    }, 1000);
                    alert("Les données ont été générées !");
                }))
        },
        generateCodeApe() {
            axios.post(this.urlGenerateCodeape)
                .then((response) => {
                    location.reload();
                    alert("Les données ont été générées !");
                })
        },
        remove() {
            axios.delete(this.urltruncate)
                .then((response) => {
                    location.reload();
                    alert("Les données ont été supprimées !");
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
        fillDataIleDeFrance() {
            this.dataPointsIleDeFrance = {
                labels: this.countsIleDeFrance,
                datasets: [{
                    label: "Départements D'Ile-de-France",
                    backgroundColor: "red",
                    data: this.countsIleDeFranceHits,
                    backgroundColor: 'transparent',
                    pointBorderColor: 'orange',
                    borderDash: [5, 5],
                    pointBackgroundColor: 'rgba(255,150,0,0.5)',
                    pointRadius: 5,
                    pointHoverRadius: 10,
                    pointHitRadius: 30,
                    pointBorderWidth: 2,
                    pointStyle: 'rectRounded',
                    borderColor: 'orange',
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
            this.getCountsIleDeFrance(),
            this.getCountsIleDeFranceHits(),
            setInterval(() => {
                this.fillData()
            }, 500),
            setInterval(() => {
                this.fillDataRegion()
            }, 500),
            setInterval(() => {
                this.fillDataIleDeFrance()
            }, 500)
    }
}
</script>

<style>
#main {
    display: flex;
}

#narrow {
    width: 49%;
}

#wide {
    flex: 1;
    width: 49%;
}

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

b {
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

.danger {
    color: #fff;
    background-color: #dc3545;
    border-color: #dc3545;
    cursor: pointer;
    padding: 15px;
    text-decoration: none;
}

.info {
    color: #fff;
    background-color: #0078e7;
    border-color: #0078e7;
    cursor: pointer;
    padding: 15px;
    text-decoration: none;
}

.info:hover {
    color: #fff;
    text-decoration: none;
    background-color: #1360a7;
}

.danger:hover {
    color: #fff;
    text-decoration: none;
    background-color: #801721;
}

.button {
    margin-bottom: 25px;
}
</style>
