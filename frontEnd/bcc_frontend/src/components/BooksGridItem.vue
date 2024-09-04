<template>
   
        <div class="book-item">
            <img src="../assets/4.jpg" />
           
            <h3 class="book-name">{{ book.title }}</h3>
            <p class="book-author"> By: {{ book.author }}</p>
            <router-link :to="'/books/' + book._id " >
                <button>More Details</button>
            </router-link>
        </div>
   
</template>
<script>
    export default {
        name: 'BookGridItem',
        props: ['book'],

    }
</script>
<style scoped>
.book-item {
    align-items: center;
    border-radius: 8px;
    box-shadow: 0px 2px 5px #888;
    display: flex;
    flex-direction: column;
    margin-bottom: 2%;
    padding: 20px;
    /* position: relative; */
    width: 32%;
  }

  .book-name {
    margin-bottom: 0;
  }

  img {
    height: 200px;
    width: 200px;
  }

  a {
    width: 100%;
  }

  button {
    width: 100%;
  }
 
</style>