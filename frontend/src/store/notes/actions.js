import {
  GET_NOTES_LIST,
  POST_NOTE_CREATE,
  DELETE_NOTE,
  PUT_NOTE_UPDATE,
} from "../../action_types";

export const getNotesList = () => {
  return {
    type: GET_NOTES_LIST,
    api: true,
  };
};

export const createNote = (body) => {
  return {
    type: POST_NOTE_CREATE,
    api: true,
    payload: body,
  };
};

export const updateNote = (payload) => {
  return {
    type: PUT_NOTE_UPDATE,
    api: true,
    payload: payload,
  };
};

export const deleteNote = (id) => {
  return {
    type: DELETE_NOTE,
    api: true,
    payload: id,
  };
};
