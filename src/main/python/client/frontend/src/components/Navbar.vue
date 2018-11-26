<template>
  <div class="container-fluid mt-4">
    <h1 class="h1">Schueler</h1>

        <table class="table table-striped">
          <thead>
            <tr>
              <th>ID (Email)</th>
              <th>Name</th>
              <th>Bild</th>
              <th>&nbsp;</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="post in posts" :key="post.id">
              <td>ID</td>
              <td>Name</td>
              <td>Bild</td>
              <td class="text-right">
              </td>
            </tr>
          </tbody>
        </table>

  </div>
</template>
