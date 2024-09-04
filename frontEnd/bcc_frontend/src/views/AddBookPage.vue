<template>
  <div id="page-wrap">
      <h1>Add Book</h1>
      <div>
          <form @submit.prevent="addBook">
              <input v-model="title" type="text" placeholder="Titel"><br>
              <input v-model="author" type="text" placeholder="Author"><br>
              <input v-model="published_date" type="text" placeholder="Publish Date"><br>
              <input v-model="isbn" type="text" placeholder="ISBN"><br>
              <select v-model="selected">
                <option disabled value="">Genre</option>
                <option>Fantasy</option>
                <option>Science fiction</option>
                <option>Historical Fiction</option>
                <option>Horror</option>
                <option>Mystery</option>
                <option>Romance</option>
              </select>
              <button >Add</button>
          </form>
          <p v-if="msg">{{ msg }}</p>
      </div>
  </div>
  
</template>

<script>
import axios from 'axios';
export default {
  name: 'AddBookPage',
  data() {
      return {
         title:'',
         author:'',
         published_date:'',
         isbn:'',
         selected:'',
         msg:''
      }
  },
  methods:{
    async addBook(){
      try {
            const response = await axios.post('http://localhost:8000/api/books/', {
            title: this.title,
            author: this.author,
            published_date: this.published_date,
            isbn: this.isbn,
            genre: this.selected })

            
            alert("Book Added")
            this.$router.push('/books')
          }
        catch (error) {
          if(error.response){
            this.msg = error.response.data.message || 'Adding Failed'
          }
          else {
            this.msg = 'Error during add book'
          }
        }
  }
},

  }
</script>
<style scoped>
  #page-wrap {
  margin-top: 16px;
  padding: 16px;
  max-width: 600px;
}

#img-wrap {
  text-align: center;
}

img {
  width: 400px;
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
select {
  padding: 10px;
  line-height: 14px;
  font-size: 16px;
  width: 100%;
  margin: 4px;
  border-radius: 8px;
}
p {
  color: red;
  text-align: center;
}
</style>
