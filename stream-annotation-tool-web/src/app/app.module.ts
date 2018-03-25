import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {MatAutocompleteModule, MatInputModule} from '@angular/material';
import {ResourcesComponent} from './resources/resources.component';
import {ResourceDetailsComponent} from './resource-details/resource-details.component';
import {RouterModule, Routes} from '@angular/router';
import {AppComponent} from './app.component';
import {ResourceService} from "./services/resource.service";
import {HttpClientModule} from "@angular/common/http";

const APP_ROUTES: Routes = [
  {path: 'resources', component: ResourcesComponent},
  {path: 'resources/:resource', component: ResourceDetailsComponent},
  {path: '', redirectTo: '/resources', pathMatch: 'full'},
]

@NgModule({
  declarations: [
    AppComponent,
    ResourcesComponent,
    ResourceDetailsComponent
  ],
  imports: [
    RouterModule.forRoot(APP_ROUTES),
    BrowserModule,
    MatInputModule,
    ReactiveFormsModule,
    MatAutocompleteModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [
    ResourceService
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
