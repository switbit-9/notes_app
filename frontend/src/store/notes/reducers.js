import {
  NOTES_LIST,
  NOTE_CREATE,
  NOTE_DELETE,
  NOTE_UPDATE,
} from "../../action_types";

const initialState = {
  list: [],
  isLoading: false,
  error: false,
};

const notes = (state = initialState, action) => {
  switch (action.type) {
    case NOTES_LIST:
      state = {
        ...state,
        isLoading: true,
      };
      break;
    case NOTES_LIST.concat("_SUCCESS"):
      list = [...state.list];
      list = [...action.payload];

      state = {
        ...state,
        list,
        isLoading: false,
      };
      break;

    case NOTES_LIST.concat("_FAILURE"):
      state = {
        ...state,
        isLoading: false,
        error: true,
      };
      break;

    case NOTE_CREATE:
      state = {
        ...state,
        isLoading: true,
      };
      break;
    case NOTE_CREATE.concat("_SUCCESS"):
      //   list = [...state.list];
      //   list = [...action.payload]

      state = {
        ...state,
        // list,
        isLoading: false,
      };
      break;

    case NOTE_CREATE.concat("_FAILURE"):
      state = {
        ...state,
        isLoading: false,
        error: true,
      };
      break;

    case NOTE_DELETE:
      state = {
        ...state,
        isLoading: true,
      };
      break;

    case NOTE_DELETE.concat("_SUCCESS"):
      state = {
        ...state,
        isLoading: false,
      };
      break;

    case NOTE_DELETE.concat("_FAILURE"):
      state = {
        ...state,
        isLoading: false,
        error: true,
      };
      break;

    case NOTE_UPDATE:
      state = {
        ...state,
        isLoading: true,
      };
      break;
    case NOTE_UPDATE.concat("_SUCCESS"):
      //   list = [...state.list];
      //   list = [...action.payload]

      state = {
        ...state,
        // list,
        isLoading: false,
      };
      break;

    case NOTE_UPDATE.concat("_FAILURE"):
      state = {
        ...state,
        isLoading: false,
        error: true,
      };
      break;
  }
  return state;
};

export default notes;
