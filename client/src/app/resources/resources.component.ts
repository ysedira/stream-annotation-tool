import {Component, OnInit, Output, EventEmitter} from '@angular/core';
import {RESOURCES} from '../mock-resources'
import {Resource}  from '../models/resource'
import {Observable} from "rxjs/Observable";
import {ResourceService} from "../services/resource.service";


@Component({
  selector: 'app-resources',
  templateUrl: './resources.component.html',
  styleUrls: ['./resources.component.css']
})
export class ResourcesComponent implements OnInit {
  resources$: Observable<Resource[]>;

  constructor(private resourceService: ResourceService) {
  }

  ngOnInit() {
    // Load Schema from server
    this.resources$ = this.resourceService.getResources()
  }
}
