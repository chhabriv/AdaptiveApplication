var express = require("express");
var cors = require('cors')

var app = express()
app.use(cors())

app.listen(3000, () => {
 console.log("Server running on port 3000");
});

app.get("/getRoutes", (req, res, next) => {

  var tempResponse = '[{"Origin":"Dublin", "Destination":"Cork"}, {"Origin":"Cork", "Destination":"Limerick"}]'


 res.json(JSON.parse(tempResponse));
});
