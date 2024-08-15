const http = require('http');
const { exec } = require('child_process');

// Função para verificar se o servidor está rodando
function checkServer() {
  return new Promise((resolve, reject) => {
    const options = {
      host: 'localhost',
      port: 8080,
      timeout: 2000,
    };

    const req = http.request(options, (res) => {
      resolve(true);
    });

    req.on('error', (err) => {
      resolve(false);
    });

    req.end();
  });
}

// Função para iniciar o servidor
function startServer() {
  exec(
    `python3 ../DistributedSystems-SocketServer/main.py`,
    (err, stdout, stderr) => {
      if (err) {
        console.error(`Error starting server: ${err.message}`);
        return;
      }
      console.log(`Server started`);
    }
  );
}

// Função para verificar se o servidor está rodando a cada 2 segundos e reiniciar se não estiver
async function heartbeat() {
  const isRunning = await checkServer();
  if (!isRunning) {
    console.log(`Server is down. Restarting...`);
    startServer();
  } else {
    console.log(`Server is running.`);
  }
}

// Define o intervalo de 2 segundos para a função heartbeat
setInterval(heartbeat, 2000);
