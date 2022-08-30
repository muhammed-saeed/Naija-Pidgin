import express from "express"; 
import bodyParser from "body-parser";
import mongoose from "mongoose";
import cors from "cors";

const app = express()
// const express = require()
app.use(bodyParser.json({limit:"30mb", extended:true}))
app.use(bodyParser.urlencoded({limit:"30mb", extended:true}))
// because we are going to send files and we can probably send requests
app.use(cors())



