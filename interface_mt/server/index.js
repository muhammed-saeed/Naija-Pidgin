import express from "express"; 
import bodyParser from "body-parser";
import mongoose from "mongoose";
import cors from "cors";

import postRoutes from "./routes/posts.js"

const app = express()
// const express = require()
app.use(bodyParser.json({limit:"30mb", extended:true}))
app.use(bodyParser.urlencoded({limit:"30mb", extended:true}))
// because we are going to send files and we can probably send requests
app.use(cors())

app.use("/posts", postRoutes)

const connection_URL = "mongodb+srv://msaeed1:tester1234@cluster0.8zqla.mongodb.net/?retryWrites=true&w=majority"
const PORT = process.env.PORT || 5000;


mongoose.connect(connection_URL, {useNewUrlParser: true, useUnifiedTopology: true})
.then(()=> app.listen(PORT, () => console.log(`Server running on PORT :${PORT}`)))
.catch((error) => console.log(error))

// mongoose.set('useFindAndModify', false);
