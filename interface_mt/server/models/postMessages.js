import mongoose  from "mongoose";
const postSchema = mongoose.Schema({
    title: String,
    message: String,
    create: String,
    tags:[String],
    selectedFile: String,
    likeCount:{
        type: Number,
        default: 0
    },
    createdAt:{ 
        type: Date,
        defaul : new Date()
    }
});

const PostMessage = mongoose.model('PostMessage', postSchema);
export default PostMessage;