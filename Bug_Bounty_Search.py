from googlesearch import search
import datetime


# List of Google dorks, including .NET applications (e.g., Hangfire) and other platforms
google_dorks = [
    # General bug bounty programs
    'inurl:"bug bounty program" India',
    'intitle:"bug bounty program" India',
    'inurl:"submit bug bounty" India',
    'site:.edu.in "bug bounty program"',
    '"bug bounty program" filetype:pdf',

    # Kibana dorks
    'intitle:"kibana" "dashboard"',
    'inurl:"/app/kibana"',
    'inurl:"/kibana" "default login"',
    '"kibana" AND "error" AND "unauthorized"',
    'inurl:"/app/kibana" "Monitoring"',
    '"Powered by Kibana" intitle:"dashboard"',

    # Prometheus dorks
    'intitle:"Prometheus" inurl:"/graph"',
    'inurl:"/alerts" "prometheus"',
    'intitle:"Prometheus Time Series Collection"',
    'inurl:"/status" "Prometheus"',
    'intitle:"Prometheus Console" "default login"',

    # Jenkins dorks
    'intitle:"Dashboard [Jenkins]"',
    'inurl:"/view/All/newJob"',
    'intitle:"Jenkins" inurl:"/manage"',
    'inurl:"/script" "Jenkins console"',
    'inurl:"/credentials" "jenkins"',
    '"powered by Jenkins" "Dashboard"',

    # Logstash dorks
    'intitle:"logstash" "log management"',
    'inurl:"/logstash/pipelines"',
    'inurl:"/logstash" "status"',
    '"logstash" AND "logs"',
    'inurl:"/logstash/monitoring"',
    
    # .NET application dorks (e.g., Hangfire)
    'intitle:"Hangfire Dashboard" "jobs"',
    'inurl:"/hangfire" "Dashboard"',
    '"Hangfire" AND "Failed Jobs"',
    'inurl:"/hangfire/retries"',
    'inurl:"/hangfire/jobs/details"',
    'intitle:"Hangfire" "default login"',
    '"Hangfire Dashboard" AND "Server Monitoring"',
    '"Unhandled Exception" AND "ASP.NET"',
    'inurl:"/logs" AND "ASP.NET Core"',
    'intitle:"error log" AND ".NET"',
    '"dotnet" AND "stack trace" AND "application logs"',
    '"Exception Details" AND "System.NullReferenceException"',
    '"Unhandled exception" AND "System.Web.HttpException"',
]
if __name__ == "__main__":
    # ANSI color code for green
    GREEN = "\033[92m"
    RESET = "\033[0m"

    # ASCII Banner with Creator Info in Green
    banner = f"""
{GREEN}
     ,-.     .              ,-.             ,-.  .       ,   .   .     
/        |             (   `           (   ` |       |   |   |   o 
|    . . |-. ,-. ;-.    `-.  ,-. ,-.    `-.  |-. ,-: | , |-  |-. . 
\    | | | | |-' |     .   ) |-' |     .   ) | | | | |<  |   | | | 
 `-' `-| `-' `-' '      `-'  `-' `-'    `-'  ' ' `-` ' ` `-' ' ' ' 
     `-'                                                           
              Created by:CybersecShakthi

 
{RESET}
"""
    print(banner)
# File to save the results
output_file = f"bug_bounty_tech_results_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"

# Search function
def search_bug_bounties(dorks, num_results=10):
    results = []
    for dork in dorks:
        print(f"Searching for: {dork}")
        try:
            for url in search(dork, num_results=num_results, lang="en"):
                results.append(url)
        except Exception as e:
            print(f"Error while searching: {e}")
    return results

# Save results to a file
def save_results(results, filename):
    with open(filename, "w") as file:
        for url in results:
            file.write(url + "\n")
    print(f"Results saved to {filename}")

if __name__ == "__main__":
    print("Starting bug bounty search with extended dorks...")
    all_results = search_bug_bounties(google_dorks, num_results=20)
    if all_results:
        save_results(all_results, output_file)
    else:
        print("No results found.")
