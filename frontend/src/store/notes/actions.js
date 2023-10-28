import {
  NOTES_LIST,
  NOTE_CREATE,
  NOTE_DELETE,
  NOTE_UPDATE,
} from "../../action_types";

export const getNotesList = () => {
  return {
    type: NOTES_LIST,
    api: true,
  };
};

export const createNote = (body) => {
  console.log(body);
  return {
    type: NOTE_CREATE,
    api: true,
    payload: body,
  };
};

export const updateNote = (payload) => {
    console.log('-------UPDATE------')
  console.log(payload);
  return {
    type: NOTE_UPDATE,
    api: true,
    payload: payload,
  };
};

export const deleteNote = (id) => {
  return {
    type: NOTE_DELETE,
    api: true,
    payload: id,
  };
};
