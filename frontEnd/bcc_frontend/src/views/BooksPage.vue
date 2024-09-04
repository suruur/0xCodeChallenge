<template>
    <div id="page-wrap">
      <books-grid :books="books"/>
      <p v-if="ErrorMsg"> {{ ErrorMsg }}</p>
    </div>
</template>

<script>
import axios from 'axios';
import BooksGrid from '../components/BooksGrid.vue'
export default { 
  
    name: 'BooksPage',
    components: { BooksGrid },
    data() {
        return {
            books:[],
            ErrorMsg:'',
        }
    },
    async created() {
        try{
            const response = await axios.get('http://localhost:8000/api/books/')
            const books = response.data
            this.books = books
            }
        catch(error){
            if(error.response)
                this.ErrorMsg = error.response.data
            else if (error.request)
                this.ErrorMsg = `No response received: ${error.request}`
            else
                this.ErrorMsg = `Error: ${error.message}`
        }
        
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
  p {
    color: red;
    text-align: center;
  }
  </style>
  