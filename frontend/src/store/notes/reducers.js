import {
  DELETE_NOTE,
  GET_NOTES_LIST,
  POST_NOTE_CREATE,
  PUT_NOTE_UPDATE,
} from "../../action_types";

const initialState = {
  list: [],
  isLoading: false,
  error: false,
};

const notes = (state = initialState, action) => {
  switch (action.type) {
    case GET_NOTES_LIST:
      state = {
        ...state,
        isLoading: true,
      };
      break;
    case GET_NOTES_LIST.concat("_SUCCESS"):

      state = {
        ...state,
        list: action.payload,
        isLoading: false,
      };
      break;

    case GET_NOTES_LIST.concat("_FAILURE"):
      state = {
        ...state,
        isLoading: false,
        error: true,
      };
      break;

    case POST_NOTE_CREATE:
      state = {
        ...state,
        isLoading: true,
      };
      break;

    case POST_NOTE_CREATE.concat("_SUCCESS"):
      list = [action.payload, ...state.list];
      state = {
        ...state,
        list,
        isLoading: false,
      };
      break;

    case POST_NOTE_CREATE.concat("_FAILURE"):
      state = {
        ...state,
        isLoading: false,
        error: true,
      };
      break;

    case DELETE_NOTE:
      state = {
        ...state,
        isLoading: true,
      };
      break;

    case DELETE_NOTE.concat("_SUCCESS"):
      const itemDeleteID = action?.payload?.id_;
      state = {
        ...state,
        list: itemDeleteID
          ? state.list.filter((item) => item.id !== itemDeleteID)
          : state.list,
        isLoading: false,
      };
      break;

    case DELETE_NOTE.concat("_FAILURE"):
      state = {
        ...state,
        isLoading: false,
        error: true,
      };
      break;

    case PUT_NOTE_UPDATE:
      state = {
        ...state,
        isLoading: true,
      };
      break;
    case PUT_NOTE_UPDATE.concat("_SUCCESS"):
      const itemUpdateID = action?.payload?.id_;

      const new_list = itemUpdateID
        ? state.list.map((item) => {
            if (item.id === itemUpdateID) {
              return action.payload;
            }
            return item;
          })
        : state.list;
      state = {
        ...state,
        list: new_list,
        isLoading: false,
      };
      break;

    case PUT_NOTE_UPDATE.concat("_FAILURE"):
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
