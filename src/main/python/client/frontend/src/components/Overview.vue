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
<form v-on:submit="createUser">
      <label> <input type="text" v-model="editForm.id"/></label>
      <label> <input type="email" v-model="editForm.email"/></label>
      <label> <input type="text" v-model="editForm.name"/></label>
      <label> <input type="text" v-model="editForm.bild"/></label>
      <button type="submit">Add</button>
    </form>
  </div>
</template>
<script>/* eslint-disable */
  import axios from 'axios';

 export default{
  data: function () {
    return {
      schueler: null,
      editForm: {
        id: '',
        email: '',
        name: '',
        bild: ''
      },
      }
    },
    methods:{
    getUser: function(self){
     axios
      .get('http://127.0.0.1:5000/schueler')
      .then(response => (this.schueler = response.data.schueler))
    },
    createUser: function() {
      var sid= this.editForm.id;
      var email= this.editForm.email;
      var benutzername=this.editForm.name;
      var bild=this.editForm.bild;
       return axios.put('http://127.0.0.1:5000/schuelerA',{id : id, email:email, name:benutzername,bild:bild});
    },

    deleteUser: function (id) {
      return axios.delete('http://127.0.0.1:5000/schuelerA',{params: {id : id}});
    }




  }
  }
</script>
