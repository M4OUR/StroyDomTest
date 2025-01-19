<template>
  <div>
    <h2>Users</h2>
    <DataTable :value="users">
      <Column field="name" header="Имя" />
      <Column field="age" header="Возраст" />
    </DataTable>

    <h2>Roles</h2>
    <DataTable :value="roles">
      <Column field="role" header="Роль" />
      <Column field="description" header="Описание" />
    </DataTable>
  </div>
</template>

<script setup>
const users = [
  { name: 'Иван', age: 25 },
  { name: 'Мария', age: 30 }
];
const roles = [
  { role: 'Администратор', description: 'Управляет системой' },
  { role: 'Пользователь', description: 'Обычный пользователь' }
];
</script>
