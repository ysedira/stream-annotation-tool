import {Triple} from './triple'

export class Resource {
	subject: string;
	type: string;
	requiredPredicates: Triple[];
	optionalPredicates: Triple[];
}
