
import Vue from "vue";

export default {
    plugins: [],
    state() {
        return {
            authors: [],
            books: []
        }
    },
    mutations: {
        SET_AUTHORS: (state, authors) => Vue.set(state, "authors", authors),
        SET_BOOKS: (state, books) => Vue.set(state, "books", books),
    },
    actions: {
        ACT_ADD_BOOK: ({ commit, state }, book) => {
            commit("SET_BOOKS", [...state.books, book]);
        },
        ACT_UPDATE_BOOK: ({ commit, state }, book) => {
            const books = state.books.map(
                (b) => {
                    if (b.id == book.id) return book;
                    return b
                } 
            );
            commit("SET_BOOKS", [...books]);
        },
        ACT_DEL_BOOK: ({ commit, state }, bookId) => {
            const books = state.books.filter(({id}) => id != bookId);
            commit("SET_BOOKS", books);
        },
        ACT_ADD_AUTHOR: ({ commit, state }, author) => {
            commit("SET_AUTHORS", [...state.authors, author]);
        },
        ACT_UPDATE_AUTHOR: ({ commit, state }, author) => {
            const authors = state.authors.map(
                (b) => {
                    if (b.id == author.id) return author;
                    return b
                } 
            );
            commit("SET_AUTHORS", authors);
        },
        ACT_DEL_AUTHOR: ({ commit, state }, authorId) => {
            const authors = state.authors.filter(({id}) => id != authorId);
            commit("SET_AUTHORS", authors);
        }

    },
    getters: {
        getAuthorByID: (state) => ((author_id) => state.authors.find(({id}) => id == author_id)),
        getBooks: (state) => {
            return state.books.map((book) => {
                const author = state.authors.find((author) => author.id === book.author_id);
                if (!author) {
                    console.warn(book)
                }
                return { ...book, author_name: author ? author.name : "Unknown" };
            });
        },
        getBooksByAuthorId: (state) => (authorId) => {
            return state.books.filter((book) => book.author_id === authorId);
        },
    }
}