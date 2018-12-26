using Discord.Commands;
using Discord;
using Discord.WebSocket;
using System.Threading.Tasks;
using System.IO;
using System.Diagnostics;
using System;

namespace discordColorBot.Modules
{
    public class Info : ModuleBase
    {
        // ~say hello -> hello
        [Command("say"), Summary("Echos a message.")]
        public async Task Say([Remainder, Summary("The text to echo")] string echo)
        {
            // ReplyAsync is a method on ModuleBase
            await ReplyAsync(echo);
        }

        [Command("ping")]
        public async Task Ping([Summary("Says Pong!")] string yeet = null)
        {
            await Context.Channel.SendMessageAsync("Pong!");
        }
        /*
        [Command("updateicon")]
        public async Task UpdateIcon([Summary("Updates the tower icon based on the tower's color")] string yeet = null)
        {
            var user = Context.User as SocketGuildUser;
            var permission = (user as IGuildUser).GuildPermissions;
            //Add ability to check user role
            {

            }
        }
        */
        [Command("towercolor")]
        public async Task TowerColor([Summary("Provides current color of tower")] string yeet = null)
        {
            Console.WriteLine("towercolor recieved");
            /*
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = @"py colorDetection.py";
            process.StartInfo = startInfo;
            process.Start();
            */

            
            //Run colorDetection on pi command line
            Process proc = new Process();
            proc.StartInfo.UseShellExecute = false;
            proc.StartInfo.RedirectStandardOutput = true;

            proc.StartInfo.FileName = "python3";
            proc.StartInfo.Arguments = "colorDetection.py";

            proc.Start();
            

            string messageText = "";

            //string colorData = File.ReadAllText(@"C: \Users\brand\Documents\Programming\utTowerColor\data.txt");
            string colorData = File.ReadAllText("data.txt");
            Console.WriteLine(colorData);
            
            //await message.Channel.SendMessageAsync("Command Recieved");

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

            else if (colorData == "3,3")
            {
                messageText = "The tower is not lit yet";
            }

            else
            {
                messageText = "Sorry, I do not know what color the tower is";
            }

            Console.WriteLine(messageText);

            await Context.Channel.SendMessageAsync(messageText);
            //await Context.Channel.SendFileAsync("out.jpg", messageText);
            //await Context.Channel.SendFileAsync("out.jpg");
            
        }

        [Command("time")]
        public async Task Time([Summary("Says Pong!")] string yeet = null)
        {
            string currentTime = DateTime.Now.ToString("h:mm tt");
            string messageText = "It is " + currentTime + " and OU still sucks!";
            await Context.Channel.SendMessageAsync(messageText);
        }


    }
}




