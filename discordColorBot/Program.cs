using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Discord;
using Discord.WebSocket;

namespace discordColorBot
{
    class Program
    {
        static void Main(string[] args)
            => new Program().MainAsync().GetAwaiter().GetResult();
        //string apikey = System.IO.File.ReadAllText(@"C: \Users\brand\Documents\Programming\utTowerColor\discordColorBot\apikey.txt");

        public async Task MainAsync()
        {
            var client = new DiscordSocketClient();

            client.Log += Log;

            string token = System.IO.File.ReadAllText(@"C: \Users\brand\Documents\Programming\utTowerColor\discordColorBot\apikey.txt");
            await client.LoginAsync(TokenType.Bot, token);
            await client.StartAsync();



            //I think this goes last
            await Task.Delay(-1);
        }

        private Task Log(LogMessage msg)
        {
            Console.WriteLine(msg.ToString());
            return Task.CompletedTask;
        }
    }
}
