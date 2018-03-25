import {Component, ViewChild} from '@angular/core';
import {Resource} from './models/resource'
import {ResourceDetailsComponent} from './resource-details/resource-details.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Stream Annotation Tool';
}
