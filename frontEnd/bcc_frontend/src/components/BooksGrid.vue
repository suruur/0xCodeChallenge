<template>
    
    
        <div class="grid-wrap">
            <books-grid-item 
                v-for="book in books"
                :key="book.id"
                :book="book" />
        </div>
 
</template>

<script>
import BooksGridItem from './BooksGridItem.vue';
    export default {
        name: 'BooksGrid',
        props: ['books'],
        components: {
            BooksGridItem,
        },


    }
</script>

<style scoped>
   .grid-wrap {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    margin-top: 16px;
  }
</style>