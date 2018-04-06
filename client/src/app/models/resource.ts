import {Triple} from './triple'

export class Resource {
  subject: string;

  type: string;
  requiredPredicates: Triple[];
  optionalPredicates: Triple[];

  constructor(subject: string, type: string, requiredPredicates: Triple[], optionalPredicates: Triple[]) {
    this.subject = subject;
    this.type = type;
    this.requiredPredicates = requiredPredicates;
    this.optionalPredicates = optionalPredicates;
  }
}
