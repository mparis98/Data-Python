<template>
  <div class="product">
    <h1>Entreprises</h1>
    <div class="pure-form">
      <fieldset>
        <input type="text" placeholder="Entreprise" v-model="name">
        <button type="submit" class="pure-button pure-button-primary" @click="addCompany">Ajouter</button>
      </fieldset>
    </div>
    <table class="pure-table">
      <thead>
        <tr>
          <th>Entreprise</th>
          <th>Suprimer</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="company in companys">
          <td style="text-align:left">{{ company.name }}</td>
          <td>
            <!-- <span class="dropdown-item" style="cursor:pointer;padding-right:10px" click="edit(item)"><i class="fa fa-edit" style="color:#20a8d8"></i></span> -->
            <span class="dropdown-item" style="cursor:pointer" @click="remove(company)"><i class="fa fa-close" style="color:red"></i></span>
          </td>
        </tr>
      </tbody>
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
