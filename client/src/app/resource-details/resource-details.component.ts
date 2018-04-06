import "rxjs/add/operator/switchMap";

import {Component, OnInit} from "@angular/core";
import {RESOURCES} from "../mock-resources";
import {Resource} from "../models/resource";
import {ActivatedRoute, ParamMap} from "@angular/router";
import {map} from "rxjs/operators/map";
import "rxjs/add/observable/of";
import "rxjs/add/operator/debounceTime";

import {Triple} from "../models/triple";
import {FormControl} from "@angular/forms";
import {Observable} from "rxjs/Observable";
import {startWith} from "rxjs/operators/startWith";
import {ResourceService} from "../services/resource.service";

@Component({
  selector: 'app-resource-details',
  templateUrl: './resource-details.component.html',
  styleUrls: ['./resource-details.component.css']
})
export class ResourceDetailsComponent implements OnInit {
  // @Input()
  resource: Resource;
  opController: FormControl = new FormControl;
  opOptions: Observable<Triple[]>;
  generatedRDF: string;

  constructor(private route: ActivatedRoute,
              private resourceService: ResourceService) {
  }

  ngOnInit() {
    this.route.paramMap.switchMap((params: ParamMap) => {
      const resourceType = params.get('resource');
      return this.resourceService.getResource(resourceType);
    }).subscribe(response => this.resource = response);

    this.opOptions = this.opController.valueChanges
      .pipe(
        startWith<string | Triple>(''),
        map(v => typeof v === 'string' ? v : v.predicate),
        map(p => p ? this.filter(p) : this.resource.optionalPredicates));
  }

  filter(val: string): Triple[] {
    return this.resource.optionalPredicates.filter(o => o.predicate.toLowerCase().indexOf(val.toLowerCase()) > -1);
  }

  opDisplay(triple?: Triple): string | undefined {
    return triple ? triple.predicate : undefined;
  }

  opAddTriple(event): void {
    event.stopPropagation();
    let triple = new Triple();
    triple.predicate = this.opController.value;
    this.resource.optionalPredicates.push(triple);
  }

  generate(event) {
    event.stopPropagation();
    this.resource.requiredPredicates.forEach(triple => triple.subject = this.resource.subject);
    this.resource.optionalPredicates.forEach(triple => triple.subject = this.resource.subject);
    this.resource.requiredPredicates = this.resource.requiredPredicates.filter(pred => pred.object);
    this.resource.optionalPredicates = this.resource.optionalPredicates.filter(pred => pred.object);
    this.resourceService.postResource(this.resource).subscribe(rdf => this.generatedRDF = rdf["content"]);

  }
}
