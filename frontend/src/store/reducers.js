import { combineReducers } from "redux";
import notes from "./notes/reducers";

const rootReducer = combineReducers({
  notes,
});

export default rootReducer;
