const express = require('express');
const bodyParser = require('body-parser');
var cors = require('cors')

const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());
app.use(cors())

// POST route
app.post('/', (req, res) => {
  const receivedData = req.body;
  console.log('Received data:', receivedData);
  res.json({username: "manasbir"});
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});