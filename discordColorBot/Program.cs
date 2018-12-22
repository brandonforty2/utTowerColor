using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Discord;
using Discord.WebSocket;
using System.IO;

namespace discordColorBot
{
    class Program
    {
        static void Main(string[] args)
            => new Program().MainAsync().GetAwaiter().GetResult();

        public async Task MainAsync()
        {
            var client = new DiscordSocketClient();

            client.Log += Log;
            client.MessageReceived += MessageReceived;

            string token = File.ReadAllText(@"C: \Users\brand\Documents\Programming\utTowerColor\discordColorBot\apikey.txt");
            await client.LoginAsync(TokenType.Bot, token);
            await client.StartAsync();

            


        async Task MessageReceived(SocketMessage message)
            {
                if (message.Content == "!towercolor")
                {
                    string strCmdText;
                    strCmdText = @"py ..\colorDetection.py";
                    System.Diagnostics.Process.Start("CMD.exe", strCmdText);

                    string colorData = File.ReadAllText(@"C: \Users\brand\Documents\Programming\utTowerColor\data.txt");
                    //await message.Channel.SendMessageAsync("Command Recieved");
                    string messageText;

                    if (colorData == "0,0")
                    {
                        messageText = "The tower is Orange today!";
                    }

                    else if (colorData == "0,1")
                    {
                        messageText = "The tower is orange and white today!";
                    }

                    else if (colorData == "1,1")
                    {
                        messageText = "The tower is white today!";
                    }

                    else if (colorData == "2,2")
                    {
                        messageText = "The tower is dark today";
                    }

                    else
                    {
                        messageText = "Sorry, I do not know what color the tower is";
                    }

                    //await message.Channel.SendMessageAsync(messageText);
                    await message.Channel.SendFileAsync(@"C: \Users\brand\Documents\Programming\utTowerColor\out.jpg", messageText);
                }
                

            }


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
