import tsgauth
import requests

if __name__ == "__main__":

    #choose which auth method you want (device or kerb)
    auth = tsgauth.oidcauth.KerbSessionAuth(use_auth_file=True)
    #auth = tsgauth.oidcauth.DeviceAuth("cmsoms-prod-public",target_client_id="cmsoms-prod",use_auth_file=True)
    lumisec = 565
    runnr = 379530
    
    lumisec_filter = f"filter[lumisection_number][GT]=-1" if lumisec is None else f"filter[lumisection_number][EQ]={lumisec}"
    oms_query=f"https://cmsoms.cern.ch/agg/api/v1/l1triggerrates?page[offset]=0&page[limit]=1&filter[run_number][EQ]={runnr}&{lumisec_filter}&group[granularity]=lumisection&fields=last_lumisection_number,l1a_total&sort=-lumisection_number"
    print(oms_query)
    r = requests.get(oms_query,**auth.authparams(),verify=False)
    print(r.json())