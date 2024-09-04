<template>
    <div id="page-wrap" v-if="book">
        
        <div id="book-details">
            <h1> {{ book.title }} </h1>
            <h3 id="author">Author: {{ book.author }} </h3>
            <p>Published Date: {{ book.published_date }}</p>
            <p>ISBN: {{ book.isbn }}</p>
            <p>Genre: {{ book.genre }}</p>
            <button  @click="editBook(book)" v-if="!editingBook">Update</button>
            <button  @click="deleteBook(book._id)">Delete</button>
        </div>


      <div  v-if="editingBook">
        <h1>Update {{editingBook.title}}</h1>
       
          <form @submit.prevent="updateBook">
              <input v-model="editingBook.title" type="text" placeholder="Titel"><br>
              <input v-model="editingBook.author" type="text" placeholder="Author"><br>
              <input v-model="editingBook.published_date" type="text" placeholder="Publish Date"><br>
              <input v-model="editingBook.isbn" type="text" placeholder="ISBN"><br>
              <input v-model="editingBook.genre" type="text" placeholder="Genre"><br>
              <button @click="updateBook(book._id)">Update</button>
         
          </form>
          <p v-if="msg"> {{ msg }} </p>
      </div>
    </div>
    <not-found-page v-else />
</template>

<script>
import axios from 'axios';
import NotFoundPage from './NotFoundPage.vue'

export default {
  components: { NotFoundPage,  },
    name: 'BookDetailPage',

    data() {
        return {
            book: {},
            newBook: {
              title: '',
              author: '',
              published_date: '',
              isbn: '',
              genre: '',
            },
            editingBook: null,
            msg: ''
        }},

    methods: {
            async fetchBook(){
              try{
                    const response = await axios.get(`http://localhost:8000/api/books/${this.$route.params.id}/`)
                    const book = response.data
                    this.book = book
            
              }catch(error)
              {
                if(error.response)
                    this.msg = error.response.data
                else if (error.request)
                    this.msg = `No response received: ${error.request}`
                else
                    this.msg = `Error: ${error.message}`
              }
                
              },

      editBook(book) {
        this.editingBook = { ...book };
      },

      updateBook() {
         axios.put(`http://127.0.0.1:8000/api/books/${this.editingBook._id}/`, this.editingBook)
          .then(() => {
          this.fetchBook()
          this.editingBook = null
        })
        .catch(error => {
          if(error.response)
                this.msg = error.response.data
        })},

      async deleteBook(){
       try{
             const result = await axios.delete(`http://localhost:8000/api/books/${this.$route.params.id}/`)
              this.$router.push('/books')
   
        }catch(error){
          if(error.response)
                this.msg = error.response.data
            else if (error.request)
                this.msg = `No response received: ${error.request}`
            else
                this.msg = `Error: ${error.message}`
        }
      },
    },
    async created (){
        this.fetchBook()
    },
}
</script>
<style scoped>
    #page-wrap {
    margin-top: 16px;
    padding: 16px;
    max-width: 600px;
  }
   #book-details {
    padding: 16px;
    position: relative;
  }
  button {
    width: 100%;
    margin-top: 2px;
  }
  input {
  padding: 10px;
  line-height: 14px;
  font-size: 16px;
  width: 100%;
  margin: 4px;
  border-radius: 8px;
}

 
  </style>
  