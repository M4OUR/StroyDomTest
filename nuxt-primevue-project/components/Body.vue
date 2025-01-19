<template>
  <div>
    <h2>Users</h2>
    <DataTable :value="users" class="mb-4">
      <Column field="name" header="Name" />
      <Column field="age" header="Age" />
    </DataTable>

    <h2>Roles</h2>
    <DataTable :value="roles">
      <Column field="role" header="Role" />
      <Column field="description" header="Description" />
    </DataTable>
  </div>
</template>

<script setup>
const users = [
  { name: 'Ivan', age: 25 },
  { name: 'Maria', age: 30 }
];

const roles = [
  { role: 'Admin', description: 'Has full access to the system' },
  { role: 'User', description: 'Can view and edit their own data' }
];
</script>

<style scoped>
h2 {
  margin-top: 1rem;
}
</style>
