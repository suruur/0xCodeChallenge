import BooksPage from "@/views/BooksPage.vue";
import BookDetailPage from "@/views/BookDetailPage.vue";
import Vue from "vue";
import VueRouter from "vue-router";
import AddBookPage from "@/views/AddBookPage.vue";

import NotFoundPage from "@/views/NotFoundPage.vue";



Vue.use(VueRouter);

const routes = [
  {
    path: "/books",
    name: "BooksPage",
    component: BooksPage,
  },
  {
    path: "/books/:id",
    name: "BookDetailPage",
    component: BookDetailPage,
  },
  {
    path: "/books/v/add",
    name: "AddBookPage",
    component: AddBookPage,
  },
  // {
  //   path: "/books/:id/update",
  //   name: "UpdateBookPage",
  //   component: UpdateBookPage,
  // },
  
  {
    path: "*",
    component: NotFoundPage,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
