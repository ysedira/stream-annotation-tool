import {Injectable} from "@angular/core";
import {Resource} from "../models/resource";
import {HttpClient, HttpParams} from "@angular/common/http";
import {environment} from "../../environments/environment";
import {Observable} from "rxjs/Observable";

@Injectable()
export class ResourceService {

  constructor(private http: HttpClient) {
  }

  getResources(): Observable<Resource[]> {
    return this.http.get<Resource[]>(environment.apiUrl)
  }

  getResource(resourceType: string): Observable<Resource> {
    const uri = [environment.apiUrl, resourceType].join('/');
    return this.http.get<Resource>(uri)
  }

  postResource(resource: Resource): Observable<string> {
    const params: HttpParams = new HttpParams();
    params.set("format", "TTL");
    return this.http.post<string>(environment.apiUrl, resource);
  }
}
