<template>
  <div class="container-fluid mt-4">
    <h1 class="h1">Schueler</h1>

        <table id="table1" class="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Email</th>
              <th>Benutzername</th>
              <th>Bild</th>
              <th><button v-on:click="getUser">Show data</button></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="s in schueler" :key="s.id">
              <td>{{ s.id}}</td>
              <td>{{ s.name }}</td>
              <td>{{ s.email }}</td>
              <td>{{ s.bild }}</td>
              <button v-on:click="deleteUser(s.id)">delete</button>
              <td class="text-right">
              </td>
            </tr>
          </tbody>
        </table>

  </div>
</template>
<script>/* eslint-disable */
  import axios from 'axios';

 export default{
  data: function () {
    return {
      schueler: null
      }
    },
    methods:{
    getUser: function(){
     axios
      .get('http://127.0.0.1:5000/schueler')
      .then(response => (this.schueler = response.data.schueler))
    },

    deleteUser: function (sid) {
      return axios.delete('http://127.0.0.1:5000/schuelerA',{params: {schueler_id : sid}});
    }
    }
  }
</script>
