<template>
  <div class="product">
    <h1>Entreprises</h1>
    <table id="example" class="display" style="width:100%">
      <thead>
            <tr>
                <th>Siren</th>
                <th>Denomination</th>
                <th>Region</th>
                <th>Ville</th>
                <th>Code Postal</th>
                <th>Numéro de département</th>
                <th>Date d'immatriculation</th>
                <th>Code APE </th>
                <th>Fiche identité </th> 
            </tr>
        </thead>
    </table>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  data () {
    return {
      name: '',
      editCompany: {
        name: ''
      },
      companys: [],
      url: 'http://localhost:5000/company/'
    }
  },
  methods: {
    getCompanys(){
      axios.get(this.url)
      .then((result) => {
        this.companys = result.data.data
      })
    },
    addCompany(){
      let data = {'name': this.name}
      axios.post(this.url, data)
      .then((result) => {
        this.companys.push(
          {
            id: result.data.data.id,
            name: result.data.data.name
          }
        )
        this.name = ''
      })
    },
    remove(company){
      axios.delete(this.url + company.id)
      .then((response) => {
        var idx = this.companys.indexOf(company)
        this.companys.splice(idx, 1)
      })
    }
  },
  mounted(){
    this.getCompanys()
  }
}
</script>

<script>
$(document).ready(function() {
      var t = $('#example').DataTable();
      var cpt = 0;
  $.ajax({
            method: 'GET',
            type: 'GET',
            url: 'http://localhost:5000/company/',
            success: function (datas) {
              datas.data.forEach(element => {
                if (cpt < 1000){
                  t.row.add([
                    element.siren,
                    element.denomination,
                    element.region,
                    element.ville,
                    element.code_postal,
                    element.num_dept,
                    element.date_immatriculation,
                    element.code_ape,
                    `<a target="_blank" href="${element.fiche_identite}">${element.fiche_identite}</a>`
                ]).draw( false );
                cpt++;
                }
              })
            }
  });
} );
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
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
  color: #42b983;
}
table {
  margin-left: auto;
  margin-right: auto;
}
</style>
