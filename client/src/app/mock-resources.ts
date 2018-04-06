import {Resource} from './models/resource';
import {Triple} from './models/triple';


const dc_subject = new Triple();
dc_subject.predicate = "dc:subject";
const dc_title = new Triple();
dc_title.predicate = "dc:title";
const dc_desc = new Triple();
dc_desc.predicate = "dc:description";

export const RESOURCES: Resource[] = [
  {
    subject: "vocals:Stream",
    type: "vocals:Stream",
    requiredPredicates: [dc_subject],
    optionalPredicates: [dc_title, dc_desc]
  },
  {
    subject: "vocals:StreamingService",
    type: "vocals:StreamingService",
    requiredPredicates: [dc_subject],
    optionalPredicates: [dc_title, dc_desc]
  }
];
