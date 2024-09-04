<template>
    <div id="nav-bar">
      <router-link to="/books" id="books-link">
        <h1>ABC BOOK MODEL</h1>
      </router-link>
      
      <div id="addbook-link">
          <router-link to="/books/v/add" ><button>Add Book</button></router-link>
          <router-link to="/books" ><button>List Books</button></router-link>
          
      
      </div>
      
    </div>
  </template>
  
  <script>
  export default {
      name: 'NavBar',
    }  
  </script>
  
  <style scoped>
    #nav-bar {
      border-bottom: 1px solid #ddd;
      height: 75px;
      width: 100%;
    }
  
    #books-link {
      text-align: center;
      display: block;
      color: black;
      font-size: 22px;
      left: 32px;
      position: absolute;
      top: 16px;
      text-decoration: none;
    }
  
    #books-link h1 {
        margin: 0;
    }
  
    #addbook-link {
      position: absolute;
      right: 16px;
      top: 16px;
      
    }
    #addbook-link {
      position: absolute;
      right: 36px;
      top: 16px;
    }
    button {
      margin: 5px;
    }
  </style>
  